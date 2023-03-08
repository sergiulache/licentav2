import { supabase } from '$lib/supabaseClient.js';
import { writable } from 'svelte/store';

const userSession = writable(null);

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

export async function logout() {
	const { error } = await supabase.auth.signOut();
	if (error) {
		alert('Error logging out');
		console.log(error);
	}
	userSession.set(null);
}

export function isAuthenticated() {
	const user = userSession;
	return user !== null;
}
