<script>
	import { onMount } from 'svelte';

	export let data;
	console.log(data);

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
			console.log('winner', result.winner);
		} else {
			console.error('Error calculating winner:', response.status, response.statusText);
		}
	}

	onMount(() => {
		calculateWinner();
	});
</script>

<p />
