<script>
	import { onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';
	import { isAuthenticated } from '$lib/auth';

	onMount(async () => {
		const loggedIn = await isAuthenticated();
		if (!loggedIn) {
			console.log(loggedIn);
			goto('/auth/login');
		}
	});
</script>

Homepage
