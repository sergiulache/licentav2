import { supabase } from '$lib/supabaseClient';
import { browser } from '$app/environment';
import { userSession } from '../../stores/userSession';
import { get } from 'svelte/store';
import { redirect } from '@sveltejs/kit';

async function getProfileData() {
	if (browser) {
		let session = get(userSession);
		if (session) {
			const userID = session.user.id; // retrieve user_id directly from session store
			//console.log('userID in profile page' + userID);
			const { data, error } = await supabase.from('users').select().eq('user_id', userID);
			if (error) throw error;
			return data[0];
		} else {
			throw redirect(302, '/auth/login');
		}
	}
}

export async function load() {
	let profileData = await getProfileData();

	// print jsonified data to console
	//console.log(JSON.stringify(profileData));
	return {
		props: {
			profileData
		}
	};
}
