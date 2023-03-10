import { supabase } from '$lib/supabaseClient.js';
import { writable } from 'svelte/store';
import { userSession } from '../stores/userSession';

export async function login(email, password) {
	try {
		const { data, error } = await supabase.auth.signInWithPassword({ email, password });

		if (error) {
			// handle error
			throw error;
		} else {
			userSession.set(data.session);
			return true;
		}
	} catch (error) {
		console.log(error);
		return false;
	}
}

supabase.auth.onAuthStateChange((event, session) => {
	console.log(event, session);
});

export async function logout() {
	const { error } = await supabase.auth.signOut();
	if (error) {
		alert('Error logging out');
		console.log(error);
	}
	userSession.set(null);
	//console.log('Clicked on logout, clearing userSession in logout() auth.js');
}

export async function isAuthenticated() {
	const { data: session, error } = await supabase.auth.getSession();

	if (error || !session || session.session === null) {
		//console.log(session);
		//throw redirect(302, '/auth/login');
		return false;
	} else {
		//console.log(session);
		return true;
	}
}

export async function getCurrentUserID() {
	const { data: session, error } = await supabase.auth.getSession();
	if (error || !session || session.session === null) {
		console.log('Error getting current user ID, not logged in');
		return false;
	} else {
		const userID = session.session.user.id;
		return userID;
	}
}
