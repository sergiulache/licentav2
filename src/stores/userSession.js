import { writable } from 'svelte/store';
import { supabase } from '../lib/supabaseClient';

const { data: session, error } = await supabase.auth.getSession();

function createSession() {
	const { subscribe, set, update } = writable(session.session);

	return {
		subscribe,
		set,
		update
	};
}

export const userSession = createSession();

// subscribe to changes in the `userSession` store

userSession.subscribe((value) => {
	console.log('userSession changed:', value);
});
