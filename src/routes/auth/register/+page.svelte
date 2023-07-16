<script>
	import { supabase } from '$lib/supabaseClient.js';
	// import transitions from svelte
	import { fade, fly, slide } from 'svelte/transition';
	import { quintOut, expoOut } from 'svelte/easing';
	import { userSession } from '../../../stores/userSession';
	import { browser } from '$app/environment';
	import { current } from '../../../stores/currentNav';

	let email = '';
	let password = '';
	let confirmPassword = '';

	let emailExists = false;
	let badFormat = false;
	let badPassword = false;
	let passFocused = false;
	let badConfirm = false;

	function verifyEmail() {
		// if email doesn't have @ or .com
		if (email.includes('@') || email.includes('.com')) {
			return true;
		} else {
			return false;
		}
	}

	const verifyPassword = () => {
		passFocused = true;
		if (password.length < 6) {
			badPassword = true;
			passFocused = false;
		} else {
			badPassword = false;
		}
	};

	const verifyConfirm = () => {
		if (confirmPassword != password) {
			badConfirm = true;
		} else {
			badConfirm = false;
		}
	};

	// async function register() {
	// 	const { user, error } = await supabase.auth.signUp({ email, password });
	// 	if (!verifyEmail()) {
	// 		badFormat = true;
	// 	} else if (error) {
	// 		emailExists = true;
	// 	} else {
	// 		emailExists = false;
	// 		console.log('user: ', user);
	// 		if (user) {
	// 			// insert the new user to the users table

	// 			const { data, error: insertError } = await supabase.from('users').insert([
	// 				{
	// 					user_id: user.id,
	// 					email: email
	// 					// ... other fields as necessary
	// 				}
	// 			]);

	// 			if (insertError) {
	// 				console.error('Error inserting to users table: ', insertError);
	// 			}
	// 		}

	// 		// redirect to login page
	// 		alert('Account created! Please login.');
	// 	}
	// }

	let accountCreated = false;

	async function register() {
		const { data, error } = await supabase.auth.signUp({ email, password });
		if (!verifyEmail()) {
			badFormat = true;
		} else if (error) {
			emailExists = true;
		} else {
			emailExists = false;
			console.log('data: ', data);
			if (data?.user) {
				// insert the new user to the users table

				const { data: insertData, error: insertError } = await supabase.from('users').insert([
					{
						user_id: data.user.id,
						email: email
						// ... other fields as necessary
					}
				]);

				if (insertError) {
					console.error('Error inserting to users table: ', insertError);
				}

				// redirect to login page
				alert('Account created! Please login.');
			}
		}
	}

	async function getUserId(email) {
		const { data, error } = await supabase.from('auth.users').select('id').eq('email', email);

		if (error) {
			console.error('Error fetching user: ', error);
			return null;
		} else {
			return data[0].id;
		}
	}

	function addToCustomUsersTable() {
		supabase.from('users').insert([
			{
				user_id: getUserId(email)
				// ... other fields as necessary
			}
		]);
	}

	$: if (accountCreated) {
		addToCustomUsersTable();
	}
</script>

<div id="registerDiv" class="grid grid-cols1 gap-4 items-center text-center justify-center">
	<div class="my-4 grid">
		<h1
			id="registerText"
			class="text-3xl font-normal text-center  text-white drop-shadow-sm max-w-xs justify-self-center"
		>
			Register a new account
		</h1>
	</div>
	<div
		class="my-1 drop-shadow-lg rounded-lg text-center grid grid-cols1 items-center justify-center"
	>
		<label for="email" class="text-white font-normal drop-shadow-sm text-xl">Email </label>
		<input
			type="email"
			placeholder="email@example.com"
			on:change={() => {
				emailExists = false;
				badFormat = false;
			}}
			bind:value={email}
			id="email"
			class="text-white justify-self-center py-2 px-3 border-2 w-72 border-neutral-800 rounded-lg bg-white/20 my-3 hover:backdrop-blur-xl  focus:border-white
        transition ease-in-out focus:-translate-y-1 focus:scale-110 focus:bg-white/10 duration-300"
		/>
		{#if badFormat}
			<p transition:slide={{ duration: 1000 }} class="text-red-100">Invalid email format</p>
		{:else if emailExists}
			<p transition:slide={{ duration: 1000 }} class="text-red-100">Email already exists</p>
		{/if}
	</div>

	<div
		class="my-1 drop-shadow-lg rounded-lg text-center grid grid-cols1 items-center justify-center"
	>
		<label for="password" class="text-white font-normal drop-shadow-sm text-xl">Password </label>
		<input
			type="password"
			on:blur={verifyPassword}
			bind:value={password}
			id="password"
			class="text-white justify-self-center py-2 px-3 border-2 w-72 border-neutral-800 rounded-lg bg-white/20 my-3 hover:backdrop-blur-xl  focus:border-white
        transition ease-in-out focus:-translate-y-1 focus:scale-110 focus:bg-white/10 duration-300"
		/>
		{#if !passFocused && badPassword}
			<p transition:slide={{ duration: 1000 }} class="text-red-100">
				Password must be at least 8 characters
			</p>
		{/if}
	</div>
	<div
		class="my-1 drop-shadow-lg rounded-lg text-center grid grid-cols1 items-center justify-center"
	>
		<label for="confirmPassword" class="text-white font-normal drop-shadow-sm text-xl"
			>Confirm password
		</label>
		<input
			type="password"
			on:blur={verifyConfirm}
			bind:value={confirmPassword}
			id="confirmPassword"
			class="text-white justify-self-center py-2 px-3 border-2 w-72 border-neutral-800 rounded-lg bg-white/20 my-3 hover:backdrop-blur-xl  focus:border-white
        transition ease-in-out focus:-translate-y-1 focus:scale-110 focus:bg-white/10 duration-300"
		/>
		{#if badConfirm}
			<p transition:slide={{ duration: 1000 }} class="text-red-100">Passwords do not match</p>
		{/if}
	</div>
	<div>
		<button
			on:click={register}
			class="border-white border-2 w-72 my-4 text-white rounded-lg p-2 transition ease-in-out  bg-teal-700 hover:-translate-y-1 hover:scale-110 hover:bg-indigo-500 duration-300"
			>Register</button
		>
	</div>
	<hr />
	<div class="my-1 flex justify-center gap-3">
		<label for="confirmPassword" class="text-white font-normal drop-shadow-sm text-nm"
			>Already have an account?
		</label>
		<a
			href="/auth/login"
			class="mb-2 text-blue-400 font-normal drop-shadow-sm text-nm transition ease-in-out rounded-lg px-2 hover:text-teal-400 hover:bg-white/5"
			>Login</a
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
