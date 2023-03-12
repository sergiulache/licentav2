import { supabase } from '$lib/supabaseClient.js';
import { writable } from 'svelte/store';
import { userSession } from '../stores/userSession';
import cookie from 'cookie';

const ACCESS_TOKEN_KEY = 'access_token';
const REFRESH_TOKEN_KEY = 'refresh_token';

export async function login(email, password) {
	try {
		const { data, error } = await supabase.auth.signInWithPassword({ email, password });

		if (error) {
			// handle error
			throw error;
		} else {
			userSession.set(data.session);
			//console.log('userSession in login() auth.js: ', userSession);
			localStorage.setItem(ACCESS_TOKEN_KEY, data.session.access_token);
			localStorage.setItem(REFRESH_TOKEN_KEY, data.session.refresh_token);
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
	localStorage.removeItem(ACCESS_TOKEN_KEY);
	localStorage.removeItem(REFRESH_TOKEN_KEY);
	userSession.set(null);
	console.log('Clicked on logout, clearing userSession in logout() auth.js');
}

export async function isAuthenticated() {
	//const { data: session, error } = await supabase.auth.getSession();

	const access_token = localStorage.getItem(ACCESS_TOKEN_KEY);
	const refresh_token = localStorage.getItem(REFRESH_TOKEN_KEY);
	//console.log(access_token);
	//console.log(refresh_token);

	if (!access_token || !refresh_token) {
		console.log('No access token or refresh token, not logged in');
		return false;
	} else {
		console.log('isAuthenticated() auth.js: TRUE');
		//userSession.set({ access_token, refresh_token });
		return true;
	}
}

export async function getCurrentUserID() {
	const { data: session, error } = await supabase.auth.getSession();
	// get current userSession store
	//const session = userSession.get();
	if (error || !session || session.session === null) {
		console.log('Error getting current user ID, not logged in');
		return false;
	} else {
		const userID = session.session.user.id;
		return userID;
	}
}
