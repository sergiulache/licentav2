<script>
	import { goto } from '$app/navigation';
	export let show = false;

	function closeModal() {
		show = false;
		goto('/profile/upload_document');
	}

	function cancelModal() {
		show = false;
		goto('/profile');
	}
</script>

<!-- This example requires Tailwind CSS v2.0+ -->
<div
	class="fixed z-10 inset-0 overflow-y-auto"
	aria-labelledby="modal-title"
	role="dialog"
	aria-modal="true"
>
	<div
		class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
	>
		<!--
      Background overlay, show/hide based on modal state.

      Entering: "ease-out duration-300"
        From: "opacity-0"
        To: "opacity-100"
      Leaving: "ease-in duration-200"
        From: "opacity-100"
        To: "opacity-0"
    -->
		<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" aria-hidden="true" />

		<!-- This element is to trick the browser into centering the modal contents. -->
		<span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true"
			>&#8203;</span
		>

		<!--
      Modal panel, show/hide based on modal state.

      Entering: "ease-out duration-300"
        From: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
        To: "opacity-100 translate-y-0 sm:scale-100"
      Leaving: "ease-in duration-200"
        From: "opacity-100 translate-y-0 sm:scale-100"
        To: "opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
    -->
		<div
			class="relative inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6"
		>
			<div class="sm:flex sm:items-start">
				<div
					class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-white-100 sm:mx-0 sm:h-10 sm:w-10"
				>
					<!-- Heroicon name: outline/exclamation -->
					<i class="fa-solid fa-circle-info text-2xl text-gray-400" />
				</div>
				<div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
					<h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">
						Upload document
					</h3>
					<div class="mt-2">
						<p class="text-sm text-gray-500">
							Before you have full access to the platform, you need to upload a document to verify
							your identity. This will also be used for bidding and creating a new auction. Other
							users will not be able to see your document.
						</p>
					</div>
				</div>
			</div>
			<div class="mt-5 sm:mt-4 sm:ml-10 sm:pl-4 sm:flex">
				<button
					on:click={closeModal}
					type="button"
					class="inline-flex justify-center w-full rounded-md border border-transparent shadow-sm px-4 py-2 bg-green-600 text-base font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 sm:w-auto sm:text-sm"
					>Upload now</button
				>
				<button
					on:click={cancelModal}
					type="button"
					class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 px-4 py-2 bg-white text-base font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
					>Cancel</button
				>
			</div>
		</div>
	</div>
</div>
