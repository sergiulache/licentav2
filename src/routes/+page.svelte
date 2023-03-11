<script>
	import { onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';
	import { isAuthenticated } from '$lib/auth';
</script>

Homepage
