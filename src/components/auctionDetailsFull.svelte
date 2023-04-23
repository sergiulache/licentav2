<script>
	import AuctionDetailsImage from './auctionDetailsImage.svelte';
	import AuctionDetailsReviewFull from './auctionDetailsReviewFull.svelte';
	import AuctionDetailsReviewStars from './auctionDetailsReviewStars.svelte';
	import { fade, fly, slide, draw } from 'svelte/transition';
	import AuctionDetailsBidStats from './auctionDetailsBidStats.svelte';
	import { userSession } from '../stores/userSession';
	import { supabase } from '$lib/supabaseClient';
	import { browser } from '$app/environment';
	import ModalSuccessAuction from './modalSuccessAuction.svelte';
	import ModalNewBid from './modalNewBid.svelte';
	import { bidsStore } from '../stores/bidsStore';
	import NotificationBidCreateSuccess from './notificationBidCreateSuccess.svelte';

	export let data;

	// console log jsonified data
	//console.log('auctionDetailsFull.svelte: ' + JSON.stringify(data.props.data.item_id));

	let showModal = false;
	let showNotification = false;
	let validExpirationDate = false;

	if (new Date(data.props.data.expiration_date) > new Date()) {
		validExpirationDate = true;
	}

	let newBid = false;
	let bid_amount;
	let bid_completion_date = new Date();
	let bid_completion_time = 30;

	let sum = 0;
	data.props.sellerReviews.forEach((review) => {
		//console.log(review.rating);
		sum += review.rating;
	});
	let total_rating = sum / data.props.sellerReviews.length;
	// round to nearest int
	let rounded_rating = Math.round(total_rating);
	//console.log(rounded_rating);

	let roundedReviewsData = {
		rating: rounded_rating
	};

	let currentUser = $userSession;
	userSession.subscribe((value) => {
		if (browser) currentUser = value.user.id;
	});

	function handleBid() {
		newBid = true;
	}

	async function handleConfirmBid() {
		let itemID = data.props.data.item_id;

		// add a new bid in supabase with the item id, bidder_id and bid amount
		const { dataNewBid, error } = await supabase
			.from('bids')
			.insert([
				{
					item_id: itemID,
					bidder_id: currentUser,
					bid_amount: bid_amount,
					bid_completion_date: bid_completion_date,
					bid_completion_time: bid_completion_time
				}
			])
			.single();

		if (!error) {
			//console.log('bid added');
			showNotification = true;
			// wait 5 seconds and then hide the modal
			setTimeout(() => {
				showNotification = false;
			}, 5000);
		} else {
			console.log('error adding bid');
		}
	}

	function handleContact() {
		//console.log('handleContact');
	}
</script>

{#if showNotification}
	<div transition:fade={{ duration: 1000 }}>
		<NotificationBidCreateSuccess />
	</div>
{/if}

<div class="bg-white p-4 sm:ml-32">
	<div class="mx-auto py-16 px-4 sm:py-6 sm:px-6 lg:max-w-7xl lg:px-8">
		<!-- Product -->
		<div class="lg:grid lg:grid-rows-1 lg:grid-cols-7 lg:gap-x-8 lg:gap-y-10 xl:gap-x-16">
			<!-- Product image -->
			<AuctionDetailsImage />
			<!-- Product details -->
			<div
				class="max-w-2xl mx-auto mt-14 sm:mt-16 lg:max-w-none lg:mt-0 lg:row-end-2 lg:row-span-2 lg:col-span-3"
			>
				<div class="flex flex-col-reverse">
					<div class="mt-4">
						<h1 class="text-2xl font-extrabold tracking-tight text-gray-900 sm:text-3xl">
							{data.props.data.title}
						</h1>

						<h2 id="information-heading" class="sr-only">Creation date</h2>
						<p class="text-sm text-gray-500 mt-2">
							Created on {new Date(data.props.data.created_at).toLocaleDateString()}
						</p>
					</div>

					<div>
						<h3 class="sr-only">Reviews</h3>
						<div class="flex items-center">
							<AuctionDetailsReviewStars data={roundedReviewsData} />
							{#if rounded_rating < 5}
								<div class="pt-4">
									{#each Array(5 - rounded_rating) as star, i}
										<!-- Heroicon name: solid/star -->
										<i class="fa-solid fa-star fa-lg text-gray-300" />
									{/each}
								</div>
							{/if}
						</div>
						<p class="sr-only">4 out of 5 stars</p>
					</div>
				</div>

				<p class="text-gray-500 mt-6">
					{data.props.data.description}
				</p>

				<!-- add section for showing current bid-->
				<div>
					<AuctionDetailsBidStats {data} />
				</div>

				<div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-4 sm:grid-cols-2">
					{#if !newBid && validExpirationDate}
						<button
							on:click={handleBid}
							type="button"
							class="w-full bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500"
							>New bid</button
						>
					{:else if newBid && validExpirationDate}
						<button
							transition:fade={{ duration: 2000 }}
							on:click={handleConfirmBid}
							type="button"
							class="w-full bg-green-600 text-white hover:bg-green-700 hover:-translate-y-1 hover:scale-105 hover:border-green-400 border-b-4 rounded-lg duration-300 "
							>Confirm Bid</button
						>
					{/if}

					<button
						on:click={handleContact}
						type="button"
						class="w-full bg-indigo-50 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-indigo-700 hover:bg-indigo-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500"
						>Contact seller</button
					>
				</div>

				<!-- add a form that slides down when the button is pressed for confirming the bid details-->
				{#if newBid && validExpirationDate}
					<div transition:slide={{ duration: 2000 }}>
						<form class="mt-10">
							<div>
								<label for="price" class="block text-sm font-medium text-gray-700">Bid Amount</label
								>
								<div class="mt-1 relative rounded-md shadow-sm">
									<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
										<span class="text-gray-500 sm:text-sm"> $ </span>
									</div>
									<input
										bind:value={bid_amount}
										type="number"
										name="price"
										id="price"
										class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
										placeholder="0.00"
										aria-describedby="price-currency"
									/>
									<div
										class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none"
									>
										<span class="text-gray-500 sm:text-sm" id="price-currency"> USD </span>
									</div>
								</div>
							</div>

							<!-- section for selecting a predicted completion date-->
							<div class="mt-6">
								<label for="about" class="block text-sm font-medium text-gray-700">
									Predicted completion date
								</label>
								<div class="mt-1">
									<input
										bind:value={bid_completion_date}
										type="date"
										name="about"
										id="about"
										class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border-gray-300 rounded-md"
									/>
								</div>
								<p class="mt-2 text-sm text-gray-500">
									When do you predict the job will be complete?
								</p>
								<div class="mt-6">
									<label for="about" class="block text-sm font-medium text-gray-700">
										Predicted time to complete
									</label>
									<div class="mt-1">
										<input
											bind:value={bid_completion_time}
											type="number"
											name="about"
											id="about"
											class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border-gray-300 rounded-md"
										/>
									</div>
									<p class="mt-2 text-sm text-gray-500">
										How many days do you predict it will take to complete the job?
									</p>
								</div>

								<div class="mt-6">
									<label for="about" class="block text-sm font-medium text-gray-700">
										Other details
									</label>
									<div class="mt-1">
										<textarea
											id="about"
											name="about"
											rows="3"
											class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 mt-1 block w-full sm:text-sm border-gray-300 rounded-md"
										/>
									</div>
									<p class="mt-2 text-sm text-gray-500">
										Any other details you'd like to share with the seller.
									</p>
								</div>
							</div>
							<!-- section for entering a predicted amount of time it will take to complete the job -->
						</form>
					</div>
				{:else if !validExpirationDate}
					<div class="mt-10">
						<p class="text-red-500">The expiration date for this auction has passed.</p>
					</div>
				{/if}

				<div class="border-t border-gray-200 mt-10 pt-10">
					<h3 class="text-sm font-medium text-gray-900">More details</h3>
					<div class="mt-4 prose prose-sm text-gray-500">
						<ul>
							<li>Located in {data.props.data.poster_city}</li>

							<li>Expires on {new Date(data.props.data.expiration_date).toLocaleDateString()}</li>

							<li>
								If possible, the job should be completed before {new Date(
									data.props.data.preferred_date
								).toLocaleDateString()}
							</li>
						</ul>
					</div>
				</div>

				<div class="border-t border-gray-200 mt-10 pt-10">
					<h3 class="text-sm font-medium text-gray-900">Terms of service</h3>
					<p class="mt-4 text-sm text-gray-500">
						Standard therms of service apply, for more information <a
							href="/terms"
							class="font-medium text-indigo-600 hover:text-indigo-500">read full license.</a
						>
					</p>
				</div>

				<div class="border-t border-gray-200 mt-10 pt-10">
					<h3 class="text-sm font-medium text-gray-900">Share</h3>
					<ul class="flex items-center space-x-6 mt-4">
						<li>
							<a
								href="/share/facebook"
								class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500"
							>
								<span class="sr-only">Share on Facebook</span>
								<i class="fa-brands fa-facebook fa-lg text-gray-400" />
							</a>
						</li>
						<li>
							<a
								href="/share/isntagram"
								class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500"
							>
								<span class="sr-only">Share on Instagram</span>
								<i class="fa-brands fa-instagram fa-lg" />
							</a>
						</li>
						<li>
							<a
								href="/share/twitter"
								class="flex items-center justify-center w-6 h-6 text-gray-400 hover:text-gray-500"
							>
								<span class="sr-only">Share on Twitter</span>
								<i class="fa-brands fa-twitter fa-lg" />
							</a>
						</li>
					</ul>
				</div>
			</div>

			<div class="w-full max-w-2xl mx-auto mt-16 lg:max-w-none lg:mt-0 lg:col-span-4">
				<div>
					<div class="border-b border-gray-200">
						<div class="-mb-px flex space-x-8" aria-orientation="horizontal" role="tablist">
							<!-- Selected: "border-indigo-600 text-indigo-600", Not Selected: "border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300" -->
							<button
								id="tab-reviews"
								class="border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300 whitespace-nowrap py-6 border-b-2 font-medium text-sm"
								aria-controls="tab-panel-reviews"
								role="tab"
								type="button">Seller Reviews</button
							>
						</div>
					</div>

					<!-- 'Customer Reviews' panel, show/hide based on tab state -->
					<div
						id="tab-panel-reviews"
						class="-mb-10"
						aria-labelledby="tab-reviews"
						role="tabpanel"
						tabindex="0"
					>
						<h3 class="sr-only">Seller Reviews</h3>

						<AuctionDetailsReviewFull {data} />
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
