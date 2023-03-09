import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';
import { isAuthenticated } from '../../../../../../../Documents/Code/licenta/licentav2/src/lib/auth';

export async function load() {
	const { data } = await supabase.from('items').select();

	const loggedIn = await isAuthenticated();
	if (!loggedIn) throw redirect(302, '/auth/login');

	return { items: data ?? [] };
}
