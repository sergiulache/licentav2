<script>
	import { logout, isAuthenticated } from '$lib/auth';
	import { redirect } from '@sveltejs/kit';
	if (isAuthenticated()) {
		logout();
		console.log(' ----- logged out');
		throw redirect(308, '/auth/login');
	} else {
		console.log(' ----- not logged in');
		throw redirect(302, '/');
	}
</script>
