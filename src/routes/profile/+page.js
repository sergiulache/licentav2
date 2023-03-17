import { supabase } from '$lib/supabaseClient';
import { getCurrentUserID } from '$lib/auth';
import { browser } from '$app/environment';
import { userSession } from '../../stores/userSession';
import { get } from 'svelte/store';
import { redirect } from '@sveltejs/kit';

async function getProfileData() {
	if (browser) {
		let loggedIn = get(userSession);
		if (loggedIn) {
			const userID = await getCurrentUserID();
			const { data, error } = await supabase.from('users').select().eq('user_id', userID);
			return data[0];
		} else {
			throw redirect(302, '/auth/login');
		}
	}
}

export async function load() {
	let profileData = await getProfileData();

	//console.log(profileData);
	return {
		profileData
	};
}
