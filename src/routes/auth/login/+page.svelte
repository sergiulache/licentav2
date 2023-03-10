<script>
	import { supabase } from '$lib/supabaseClient.js';
	import { login } from '$lib/auth.js';
	import {goto} from '$app/navigation';

	// import transitions from svelte
	import { fade, fly, slide } from 'svelte/transition';
	import { quintOut, expoOut } from 'svelte/easing';

	let email = '';
	let password = '';

	let badCredentials = false;

	/*
	function login() {
		supabase.auth.signInWithPassword({ email, password }).then(({ data, error }) => {
			if (error) {
				badCredentials = true;
			} else {
				// redirect to login page
				console.log(data);
				alert('Logged in!');
			}
		});
	}
    */
	function handleLogin() {
		login(email, password).then((success) => {
			if (success) {
				console.log('Logged in!');
				goto('/auctions')
			} else {
				badCredentials = true;
			}
		});
	}
</script>

<div id="registerDiv" class="grid grid-cols1 gap-4 items-center text-center justify-center">
	<div class="my-4 grid">
		<h1
			id="registerText"
			class="text-3xl font-normal text-center  text-white drop-shadow-sm max-w-xs justify-self-center"
		>
			Login to an existing account
		</h1>
	</div>
	<div
		class="my-1 drop-shadow-lg rounded-lg text-center grid grid-cols1 items-center justify-center"
	>
		<label for="email" class="text-white font-normal drop-shadow-sm text-xl">Email </label>
		<input
			type="email"
			bind:value={email}
			id="email"
			class="text-white justify-self-center py-2 px-3 border-2 w-72 border-neutral-800 rounded-lg bg-white/20 my-3 hover:backdrop-blur-xl  focus:border-white
        transition ease-in-out focus:-translate-y-1 focus:scale-110 focus:bg-white/10 duration-300"
		/>
	</div>
	<div
		class="my-1 drop-shadow-lg rounded-lg text-center grid grid-cols1 items-center justify-center"
	>
		<label for="password" class="text-white font-normal drop-shadow-sm text-xl">Password </label>
		<input
			type="password"
			bind:value={password}
			id="password"
			class="text-white justify-self-center py-2 px-3 border-2 w-72 border-neutral-800 rounded-lg bg-white/20 my-3 hover:backdrop-blur-xl  focus:border-white
        transition ease-in-out focus:-translate-y-1 focus:scale-110 focus:bg-white/10 duration-300"
		/>
		{#if badCredentials}
			<p transition:slide={{ duration: 1000 }} class="text-red-100">Invalid email or password</p>
		{/if}
	</div>
	<div>
		<button
			on:click={handleLogin}
			class="border-white border-2 w-72 my-4 text-white rounded-lg p-2 transition ease-in-out  bg-teal-700 hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 duration-300"
			>Login</button
		>
	</div>
	<hr />
	<div class="my-1 flex justify-center gap-3">
		<label for="confirmPassword" class="text-white font-normal drop-shadow-sm text-nm"
			>Don't have an account?
		</label>
		<a
			href="/auth/register"
			class="mb-2 text-blue-400 font-normal drop-shadow-sm text-nm transition ease-in-out rounded-lg px-2 hover:text-teal-400 hover:bg-white/5"
			>Register</a
		>
	</div>
</div>

<style>
	#registerText {
		/*-webkit-text-stroke: 1px black;*/
		text-shadow: 2px 2px 4px black;
		font-weight: 300;
	}
	label,
	button,
	h1,
	a {
		text-shadow: 2px 2px 4px black;
		font-weight: 500;
	}
	input:focus {
		outline: none;
	}
	input,
	p {
		text-shadow: 2px 2px 4px black;
	}
</style>
