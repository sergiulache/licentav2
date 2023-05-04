<script>
	import { onMount } from 'svelte';
	import { supabase } from '$lib/supabaseClient';
	import { goto } from '$app/navigation';

	export let data;
	console.log(data);
	$: winnerInformation = {};
	$: first_name = '';
	$: last_name = '';
	$: email = '';

	async function getWinnerData(id) {
		const { data: winnerInformation, error: error } = await supabase
			.from('users')
			.select('first_name, last_name, email')
			.eq('user_id', id);
		console.log('data', data);
		console.log('error', error);
		return winnerInformation;
	}
	async function calculateWinner() {
		const response = await fetch('http://127.0.0.1:8000/calculate_winner', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			// body is data to json
			body: JSON.stringify(data)
		});

		if (response.ok) {
			const result = await response.json();
			//const winner = result.winner;
			console.log('winner', result.winner.bidder_id);
			// select name, last name and email from users where user_id = winner
			winnerInformation = await getWinnerData(result.winner.bidder_id);
			console.log('winnerInformation', winnerInformation);
			first_name = winnerInformation[0].first_name;
			last_name = winnerInformation[0].last_name;
			email = winnerInformation[0].email;
		} else {
			console.error('Error calculating winner:', response.status, response.statusText);
		}
	}

	onMount(() => {
		calculateWinner();
	});

	function confirmIdentity() {
		goto('/confirm_identity');
	}
</script>

<div class="bg-white p-4 sm:ml-64">
	<div class="mx-auto py-16 px-4 sm:py-6 sm:px-6 lg:max-w-7xl lg:px-8">
		<h1 class="text-2xl font-bold">Winner</h1>
		<p class="text-gray-500">The winner of the auction:</p>
		<p>{first_name + ' '} {last_name}</p>
		<p>{email}</p>
		{#if first_name}
			<button
				on:click={confirmIdentity}
				type="button"
				class="mt-6 w-full p-4 rounded-md border border-gray-300bg-white text-base font-medium text-gray-700 shadow-sm hover:bg-green-50 hover:ring-green-500 hover:ring-offset-2  hover:ring-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:w-auto sm:text-sm"
				>Confirm Identity</button
			>
		{/if}
	</div>
</div>
