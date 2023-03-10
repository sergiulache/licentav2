import { supabase } from '$lib/supabaseClient';
import { isAuthenticated } from '$lib/auth';

export async function load() {
	const { data } = await supabase.from('items').select();

	let loggedIn = await isAuthenticated();
	console.log(loggedIn);

	return {
		items: data ?? []
	};
}
