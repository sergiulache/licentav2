import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';

export async function load() {
	const { data } = await supabase.from('items').select();

	const { data: session, error } = await supabase.auth.getSession();

	if (error || !session || session.session === null) {
		console.log(session);
		throw redirect(302, '/auth/login');
	}
	console.log(session);

	return { items: data ?? [] };
}
