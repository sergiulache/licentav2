<script>
	import { onMount } from 'svelte';

	async function calculateWinner() {
		let random_json = JSON.stringify({ data: 'test test original' });
		const response = await fetch('http://127.0.0.1:8000/calculate_winner', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: random_json
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
