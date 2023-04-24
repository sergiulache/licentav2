<script>
	import AuctionDetailsReviewStars from './auctionDetailsReviewStars.svelte';

	export let data;
</script>

{#if data.props.sellerReviews[0].reviewer_name && data.props.sellerReviews.length > 0 && data.props.sellerReviews[0].reviewer_name != '' && data.props.sellerReviews}
	{#each data.props.sellerReviews as review}
		<div class="flex text-sm text-gray-500 space-x-4">
			<div class="flex-none py-10">
				<i class="fa-solid fa-user fa-2xl pt-1" />
			</div>
			<div class="py-8">
				<h3 class="font-medium text-gray-900">{review.reviewer_name}</h3>
				<p>
					<time datetime="2021-07-16"
						>{new Date(review.review.created_at).toLocaleDateString()}</time
					>
				</p>

				<AuctionDetailsReviewStars data={review.review} />
				<p class="sr-only">5 out of 5 stars</p>

				<div class="mt-4 prose prose-sm max-w-none text-gray-500">
					<p>
						{review.review.text}
					</p>
				</div>
			</div>
		</div>
		<hr />
	{/each}
{:else}
	<div class="flex text-sm text-gray-500 space-x-4">
		<div class="flex-none py-10 flex">
			<i class="fa-solid fa-person-circle-question fa-2xl pt-1" />
			<div class="py-2 pl-4">
				<h3 class="font-medium text-gray-900">No reviews yet</h3>
			</div>
		</div>
	</div>
{/if}
