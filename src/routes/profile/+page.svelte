<script>
	import { goto } from '$app/navigation';
	import { supabase } from '$lib/supabaseClient';
	import ModalSuccessProfile from '../../components/modalSuccessProfile.svelte';
	export let data;

	// Initialize the variables
	let username, about, first_name, last_name, country, address, city, state, zip;
	let showModal = false;

	$: if (data && data.props && data.props.profileData) {
		// When data is available, set the variables
		username = data.props.profileData.username ? data.props.profileData.username : '';
		about = data.props.profileData.about ? data.props.profileData.about : '';
		first_name = data.props.profileData.first_name ? data.props.profileData.first_name : '';
		last_name = data.props.profileData.last_name ? data.props.profileData.last_name : '';
		country = data.props.profileData.country ? data.props.profileData.country : '';
		address = data.props.profileData.address ? data.props.profileData.address : '';
		city = data.props.profileData.city ? data.props.profileData.city : '';
		state = data.props.profileData.state ? data.props.profileData.state : '';
		zip = data.props.profileData.zip ? data.props.profileData.zip : '';
	}

	function handleCancel() {
		goto('/auctions');
	}

	async function handleSave() {
		let userID = data.props.profileData.user_id;
		// update supabase user table with new data, for this user ID
		const { dataUpdate, error } = await supabase
			.from('users')
			.update({ username, about, first_name, last_name, country, address, city, state, zip })
			.eq('user_id', userID)
			.select();

		if (error != null) {
			console.log('error: ', error);
		} else {
			showModal = true;
		}
	}

	function uploadDocument() {
		goto('/profile/upload_document');
	}
</script>

<ModalSuccessProfile show={showModal} />

<form class="space-y-8 divide-y divide-gray-200 p-5 ml-64 sm:ml-64">
	<div class="space-y-8 divide-y divide-gray-200 sm:space-y-5 border-2 border-gray rounded-xl p-3">
		<div>
			<div>
				<h3 class="text-lg leading-6 font-medium text-gray-900">Profile</h3>
				<p class="mt-1 max-w-2xl text-sm text-gray-500">
					This information will be displayed publicly so be careful what you share.
				</p>
			</div>

			<div class="mt-6 sm:mt-5 space-y-6 sm:space-y-5">
				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="username" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						Username
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<div class="max-w-lg flex rounded-md shadow-sm">
							<input
								bind:value={username}
								type="text"
								name="username"
								id="username"
								autocomplete="username"
								class="flex-1 block w-full focus:ring-indigo-500 focus:border-indigo-500 min-w-0 rounded-md  sm:text-sm border-gray-300"
							/>
						</div>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="about" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						About
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<textarea
							bind:value={about}
							id="about"
							name="about"
							rows="3"
							class="max-w-lg shadow-sm block w-full focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md"
						/>
						<p class="mt-2 text-sm text-gray-500">Write a few sentences about yourself.</p>
					</div>
				</div>
			</div>
		</div>

		<div class="pt-8 space-y-6 sm:pt-10 sm:space-y-5">
			<div>
				<h3 class="text-lg leading-6 font-medium text-gray-900">Personal Information</h3>
				<p class="mt-1 max-w-2xl text-sm text-gray-500">
					General information which will be shared with your customers.
				</p>
			</div>
			<div class="space-y-6 sm:space-y-5">
				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="first-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						First name
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={first_name}
							type="text"
							name="first-name"
							id="first-name"
							autocomplete="given-name"
							class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="last-name" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						Last name
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={last_name}
							type="text"
							name="last-name"
							id="last-name"
							autocomplete="family-name"
							class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="country" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						Country
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<select
							bind:value={country}
							id="country"
							name="country"
							autocomplete="country-name"
							class="max-w-lg block focus:ring-indigo-500 focus:border-indigo-500 w-full shadow-sm sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						>
							<option>United States</option>
							<option>Canada</option>
							<option>Mexico</option>
						</select>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label
						for="street-address"
						class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"
					>
						Street address
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={address}
							type="text"
							name="street-address"
							id="street-address"
							autocomplete="street-address"
							class="block max-w-lg w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="city" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						City
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={city}
							type="text"
							name="city"
							id="city"
							autocomplete="address-level2"
							class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="region" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						State / Province
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={state}
							type="text"
							name="region"
							id="region"
							autocomplete="address-level1"
							class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>

				<div
					class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5"
				>
					<label for="postal-code" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
						ZIP / Postal code
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<input
							bind:value={zip}
							type="text"
							name="postal-code"
							id="postal-code"
							autocomplete="postal-code"
							class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
						/>
					</div>
				</div>
				<div
					class="sm:grid sm:grid-cols-5 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-0"
				>
					<button
						on:click={uploadDocument}
						type="button"
						class="mt-6 w-full p-4 rounded-md border border-gray-300bg-white text-base font-medium text-gray-700 shadow-sm hover:bg-green-50 hover:ring-green-500 hover:ring-offset-2  hover:ring-2 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:w-auto sm:text-sm"
						>Upload verification document</button
					>
				</div>
			</div>
		</div>
		<div class="pt-5">
			<div class="flex justify-end">
				<button
					on:click={handleCancel}
					type="button"
					class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
					>Cancel</button
				>
				<button
					on:click={handleSave}
					type="submit"
					class="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
					>Save</button
				>
			</div>
		</div>
	</div>
</form>
