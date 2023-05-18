<script>
	import { supabase } from '$lib/supabaseClient';
	import { fade, slide } from 'svelte/transition';
	import { userSession } from '../../../stores/userSession';
	import { documentUpload } from '../../../stores/documentUpload';
	import { browser } from '$app/environment';
	import toast, { Toaster } from 'svelte-french-toast';

	$: photoSupabaseURL = null;
	$: viewPhoto = false;
	$: photoVersion = 0;
	$: lastModified = null;
	let currentUser = $userSession;
	userSession.subscribe((value) => {
		if (browser) currentUser = value.user.id;
	});

	let testDocumentStore = $documentUpload;
	documentUpload.subscribe((value) => {
		if (browser) testDocumentStore = value;
	});

	$: console.log('value in document store' + JSON.stringify(testDocumentStore));

	async function uploadProfilePhoto(event) {
		const file = event.target.files[0];
		if (!file) return;

		const {
			data: { user }
		} = await supabase.auth.getUser();

		if (!user) return;

		// You can customize the file path as needed
		const filePath = `profile-photos/${user.id}/document`;

		// Upload the new photo and replace the existing one if it exists
		const { error } = await supabase.storage.from('user-photos').upload(filePath, file, {
			upsert: true
		});

		if (error) {
			console.error('Error uploading profile photo:', error);
		} else {
			console.log('Profile photo uploaded successfully');
			photoVersion += 1;
			// You can save the file URL to the user's profile in your database if needed
			// const fileUrl = supabase.storage.from('<your_bucket_name>').getPublicUrl(filePath);
		}
	}

	async function getUserProfilePhoto(userId) {
		const folderPath = `profile-photos/${userId}/`;
		const { data: contents, error } = await supabase.storage.from('user-photos').list(folderPath);

		if (error) {
			console.error('Error fetching profile photo:', error);
			return null;
		}

		if (contents && contents.length > 0) {
			const validFile = contents.find((file) => file.name !== '.emptyFolderPlaceholder');
			if (validFile) {
				const fileUrl = `https://yqyheutdblzkrxymbhpw.supabase.co/storage/v1/object/public/user-photos/${folderPath}${validFile.name}`;
				return { photoURL: fileUrl, lastModified: validFile.metadata.lastModified };
			}
		}

		return null;
	}

	getUserProfilePhoto(currentUser).then((result) => {
		if (result && result.photoURL) {
			photoSupabaseURL = result.photoURL;
			lastModified = result.lastModified;
		} else {
			console.log('User does not have a profile photo.');
		}
	});

	function handleViewPhoto() {
		viewPhoto = !viewPhoto;
	}

	function handleFileChange(event) {
		toast.promise(uploadProfilePhoto(event), {
			loading: 'Uploading...',
			success: 'Profile photo uploaded successfully!',
			error: 'Error uploading profile photo.'
		});
	}
</script>

<Toaster />

<div class="space-y-6 p-4 sm:ml-64">
	<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
		<h1 class="text-xl leading-6 font-medium text-gray-900">Upload a document</h1>

		<p class="mt-5 max-w-2xl text-sm text-gray-500">
			Please upload any of the valid documents below. This photo will be used for confirming your
			identity when bidding on auctions.
		</p>
		<ul class="grid grid-cols-1 my-5 gap-6 sm:grid-cols-2 lg:grid-cols-3">
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-6">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">ID Card</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-green-800 text-xs font-medium bg-green-100 rounded-full"
								>Valid</span
							>
						</div>
						<p class="mt-3 text-gray-500 text-sm truncate">Standard Issue ID Card</p>
					</div>
					<img class="h-20" src="/IDCard.png" alt="" />
				</div>
			</li>
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-6">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">Drivers License</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-green-800 text-xs font-medium bg-green-100 rounded-full"
								>Valid</span
							>
						</div>
						<p class="mt-3 text-gray-500 text-sm truncate">International Driving Permits</p>
					</div>
					<img class="h-20" src="/driverLicense.png" alt="" />
				</div>
			</li>
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-6">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">Passport</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-green-800 text-xs font-medium bg-green-100 rounded-full"
								>Valid</span
							>
						</div>
						<p class="mt-3 text-gray-500 text-sm truncate">National Issue Passport</p>
					</div>
					<img
						class="h-20"
						src="https://static.vecteezy.com/system/resources/previews/014/943/384/original/passport-travel-documents-for-immigration-officers-in-the-airport-before-traveling-free-png.png"
						alt=""
					/>
				</div>
			</li>
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-24">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">Document Copies</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-red-800 text-xs font-medium bg-red-100 rounded-full"
								>Invalid</span
							>
						</div>
						<p class="mt-2 text-gray-500 text-sm truncate">Not using the original document</p>
					</div>
					<img class="h-24" src="/documentCopies.png" alt="" />
				</div>
			</li>
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-24">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">Student Card</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-red-800 text-xs font-medium bg-red-100 rounded-full"
								>Invalid</span
							>
						</div>
						<p class="mt-2 text-gray-500 text-sm truncate">Any University Issued Cards</p>
					</div>
					<img class="h-24" src="/studentCard.png" alt="" />
				</div>
			</li>
			<li class="col-span-1 bg-white rounded-lg shadow-lg border divide-y divide-gray-200">
				<div class="w-full flex items-center justify-between p-6 space-x-24">
					<div class="flex-1 truncate">
						<div class="flex items-center space-x-3">
							<h3 class="text-gray-900 text-sm font-medium truncate">Work Permit</h3>
							<span
								class="flex-shrink-0 inline-block px-2 py-0.5 text-red-800 text-xs font-medium bg-red-100 rounded-full"
								>Invalid</span
							>
						</div>
						<p class="mt-2 text-gray-500 text-sm truncate">Any type of granted work permit</p>
					</div>
					<img class="h-24" src="/workPermit.png" alt="" />
				</div>
			</li>
		</ul>
		{#if photoSupabaseURL}
			<div class="mt-2">
				<i class="fa-solid fa-check text-green-500" />
				<p class="flex-shrink-0 inline-block px-2 py-0.5">You have already uploaded a document.</p>
				<div>
					<!-- button for showing a dropdown with the current photo-->
					<button
						on:click={handleViewPhoto}
						type="button"
						class="relative bg-white rounded-full shadow-sm px-2 py-0.5 my-3 border border-gray-300 text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
						id="menu-button"
						aria-expanded="false"
						aria-haspopup="true"
					>
						View current photo</button
					>
				</div>
			</div>
		{/if}
		{#if viewPhoto}
			<div transition:slide={{ duration: 1000 }} class="mt-2 flex items-center">
				<img class="h-40" src={`${photoSupabaseURL}?v=${lastModified}`} alt="" />
			</div>
			<div>
				<i class="fa-solid fa-circle-info text-lg text-gray-600" />
				<h2
					class="text-lg leading-6 font-medium text-gray-900 flex-shrink-0 inline-block px-2 py-0.5 my-3"
				>
					You can replace your current photo by uploading another image below.
				</h2>
			</div>
		{/if}
		<div>
			<p class="block text-sm font-medium text-gray-700" />
			<div
				class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md"
			>
				<div class="space-y-1 text-center">
					<i class="fa-regular fa-file-image fa-2xl text-gray-500 mb-2" />
					<div class="flex text-sm text-gray-600">
						<label
							for="file-upload"
							class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
						>
							<span>Upload a file</span>
							<input
								id="file-upload"
								name="file-upload"
								type="file"
								class="sr-only"
								on:change={handleFileChange}
							/>
						</label>
						<p class="pl-1">or drag and drop</p>
					</div>
					<p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
				</div>
			</div>
		</div>
	</div>
</div>
