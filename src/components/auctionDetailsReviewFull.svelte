<script>
	import AuctionDetailsReviewStars from './auctionDetailsReviewStars.svelte';

	export let data;
</script>

{#each data.props.sellerReviews as review}
	<div class="flex text-sm text-gray-500 space-x-4">
		<div class="flex-none py-10">
			<i class="fa-solid fa-user fa-2xl pt-1" />
		</div>
		<div class="py-8">
			<h3 class="font-medium text-gray-900">{review.reviewer_name}</h3>
			<p><time datetime="2021-07-16">{new Date(review.created_at).toLocaleDateString()}</time></p>

			<AuctionDetailsReviewStars data={review} />
			<p class="sr-only">5 out of 5 stars</p>

			<div class="mt-4 prose prose-sm max-w-none text-gray-500">
				<p>
					{review.text}
				</p>
			</div>
		</div>
	</div>
	<hr />
{/each}
