import { supabase } from '$lib/supabaseClient';
import { redirect } from '@sveltejs/kit';
import { isAuthenticated } from '$lib/auth';

export async function load() {
	const { data } = await supabase.from('items').select();

	return {
		items: data ?? []
	};
}
