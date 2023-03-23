<script>
	export let data;

	// console log jsonified data
	//console.log('data from auctionDetailsReviewStars.svelte');
	//console.log(JSON.stringify(data.rating));
</script>

<div class="flex items-center mt-4">
	{#each Array(data.rating) as star, i}
		<!-- Heroicon name: solid/star -->
		<i class="fa-solid fa-star fa-lg text-yellow-400" />
	{/each}
</div>
