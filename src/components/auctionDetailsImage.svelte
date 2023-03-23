<script>
	import { onMount } from 'svelte';

	// get all images from /src/auctionImages
	// and store them in an array
	const images = import.meta.globEager('/src/auctionImages/*.jpg');

	// select a random image from the array
	const randomImage =
		images[Object.keys(images)[Math.floor(Math.random() * Object.keys(images).length)]];
</script>

<div class="lg:row-end-1 lg:col-span-4">
	<div class="aspect-w-4 aspect-h-3 rounded-lg bg-gray-100 overflow-hidden">
		<img
			src={randomImage.default}
			alt="Sample of 30 icons with friendly and fun details in outline, filled, and brand color styles."
			class="object-center object-contain "
		/>
	</div>
</div>
