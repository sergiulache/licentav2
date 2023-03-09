import { redirect } from '@sveltejs/kit';
import { isAuthenticated, logout } from '$lib/auth';

export async function load() {
	const loggedIn = await isAuthenticated();
	if (!loggedIn) {
		throw redirect(302, '/auth/login');
	} else {
		await logout();
		throw redirect(302, '/auth/login');
	}
}
