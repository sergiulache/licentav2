<script>
	import { goto } from '$app/navigation';
	import { fade, slide } from 'svelte/transition';

	$: show = true;

	function digitalSignature() {
		goto('/digital_signature');
	}

	function dismiss() {
		show = false;
	}
</script>

{#if show}
	<div class="space-y-6 p-4 sm:ml-64" transition:slide={{ duration: 1000 }}>
		<div class="rounded-md bg-green-50 p-4">
			<div class="flex">
				<div class="flex-shrink-0">
					<!-- Heroicon name: solid/check-circle -->
					<svg
						class="h-5 w-5 text-green-400"
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 20 20"
						fill="currentColor"
						aria-hidden="true"
					>
						<path
							fill-rule="evenodd"
							d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
							clip-rule="evenodd"
						/>
					</svg>
				</div>
				<div class="ml-3">
					<h3 class="text-sm font-medium text-green-800">Verification complete!</h3>
					<div class="mt-2 text-sm text-green-700">
						<p>Your identity has been successfully verified.</p>
					</div>
					<div class="mt-4">
						<div class="-mx-2 -my-1.5 flex">
							<button
								on:click={digitalSignature}
								type="button"
								class="bg-green-50 px-2 py-1.5 rounded-md text-sm font-medium text-green-800 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-green-50 focus:ring-green-600"
								>Complete digital signature</button
							>
							<button
								on:click={dismiss}
								type="button"
								class="ml-3 bg-green-50 px-2 py-1.5 rounded-md text-sm font-medium text-green-800 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-green-50 focus:ring-green-600"
								>Dismiss</button
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}
