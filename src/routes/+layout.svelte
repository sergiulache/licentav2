<script>
	import '../app.css';
	import NavbarFull from '../components/navbarFull.svelte';
	import { userSession } from '../stores/userSession.js';

	import { onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
	import { goto } from '$app/navigation';
	import { isAuthenticated } from '$lib/auth';
	import NavbarIn from '../components/navbarIN.svelte';
	import NavbarOut from '../components/navbarOUT.svelte';

	/*
	let loggedIn = false;
	onMount(async () => {
		loggedIn = await isAuthenticated();
		if (!loggedIn) {
			console.log('Layout logged in: ' + loggedIn);
		}
	});
	loggedIn = loggedIn;
	*/
	let loggedIn = $userSession;
	loggedIn = loggedIn;
	userSession.subscribe((value) => {
		loggedIn = value;
	});
</script>

<svelte:head>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
		/* import Golos text font */
		@import url('https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700;800;900&display=swap');
	</style>
	<link
		href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.3/flowbite.min.css"
		rel="stylesheet"
	/>
</svelte:head>

<main>
	{#if loggedIn}
		<NavbarIn />
	{:else}
		<NavbarOut />
	{/if}
	<slot />
</main>

<style>
	main {
		display: flexbox;
		height: 100%;
		width: 100%;
		place-items: center;
		align-items: center;
		/*background: linear-gradient(-135deg, #c850c0, #4158d0); */
	}

	/* set font family */
	* {
		font-family: 'Golos text', sans-serif;
	}
</style>
