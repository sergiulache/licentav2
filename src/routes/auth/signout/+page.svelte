<script>
	import { logout, isAuthenticated } from '$lib/auth';
	import { navigate } from 'svelte-routing';
	if (isAuthenticated()) {
		logout();
		console.log(' ----- logged out -------');
	}
	navigate('/auth/login', { replace: true });
</script>
