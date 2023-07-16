import { supabase } from '$lib/supabaseClient';
import { browser } from '$app/environment';
import { userSession } from '../../stores/userSession';
import { get } from 'svelte/store';
import { redirect } from '@sveltejs/kit';

let userID;

if (browser) {
	let session = get(userSession);
	if (session) {
		userID = session.user.id; // retrieve user_id directly from session store
	} else {
		throw redirect(302, '/auth/login');
	}
}

export async function load() {
	let notifications = [];
	if (userID) {
		const { data, error } = await supabase.rpc('get_notifications_with_titles', {
			p_user_id: userID
		});
		if (error) {
			console.log('Error: ', error);
		} else {
			console.log('data', JSON.stringify(data));
			notifications = data;
		}
	}
	return {
		props: {
			notifications
		}
	};
}
