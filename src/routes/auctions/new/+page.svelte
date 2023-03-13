<div class="space-y-6 p-4 sm:ml-64">
	<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
		<div class="md:grid md:grid-cols-3 md:gap-6">
			<div class="md:col-span-1">
				<h3 class="text-lg font-medium leading-6 text-gray-900">Auction details</h3>
				<p class="mt-1 text-sm text-gray-500">
					This information will be displayed publicly so be careful what you share.
				</p>
			</div>
			<div class="mt-5 md:mt-0 md:col-span-2">
				<form class="space-y-6" action="#" method="POST">
					<div class="grid grid-cols-3 gap-6">
						<div class="col-span-3 sm:col-span-2">
							<label for="auction-title" class="block text-sm font-medium text-gray-700">
								Title
							</label>
							<div class="mt-1 flex rounded-md shadow-sm">
								<input
									type="text"
									name="auction-title"
									id="auction-title"
									class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
									placeholder="Example title..."
								/>
							</div>
						</div>
					</div>

					<div>
						<label for="description" class="block text-sm font-medium text-gray-700">
							Description
						</label>
						<div class="mt-1">
							<textarea
								id="description"
								name="description"
								rows="3"
								class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-300 rounded-md"
								placeholder="Auction details..."
							/>
						</div>
						<p class="mt-2 text-sm text-gray-500">
							Brief description for your auction. URLs are hyperlinked.
						</p>
					</div>

					<div>
						<label class="block text-sm font-medium text-gray-700"> Cover photo </label>
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
										<input id="file-upload" name="file-upload" type="file" class="sr-only" />
									</label>
									<p class="pl-1">or drag and drop</p>
								</div>
								<p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
							</div>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>

	<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
		<div class="md:grid md:grid-cols-3 md:gap-6">
			<div class="md:col-span-1">
				<h3 class="text-lg font-medium leading-6 text-gray-900">Personal Information</h3>
				<p class="mt-1 text-sm text-gray-500">
					Use a permanent address where you can receive mail.
				</p>
			</div>
			<div class="mt-5 md:mt-0 md:col-span-2">
				<form action="#" method="POST">
					<div class="grid grid-cols-6 gap-6">
						<div class="col-span-6 sm:col-span-3">
							<label for="first-name" class="block text-sm font-medium text-gray-700"
								>First name</label
							>
							<input
								type="text"
								name="first-name"
								id="first-name"
								autocomplete="given-name"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>

						<div class="col-span-6 sm:col-span-3">
							<label for="last-name" class="block text-sm font-medium text-gray-700"
								>Last name</label
							>
							<input
								type="text"
								name="last-name"
								id="last-name"
								autocomplete="family-name"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>

						<!--
						<div class="col-span-6 sm:col-span-4">
							<label for="email-address" class="block text-sm font-medium text-gray-700"
								>Email address</label
							>
							<input
								type="text"
								name="email-address"
								id="email-address"
								autocomplete="email"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>
						-->

						<div class="col-span-6 sm:col-span-3">
							<label for="country" class="block text-sm font-medium text-gray-700">Country</label>
							<select
								id="country"
								name="country"
								autocomplete="country-name"
								class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
							>
								<option>United States</option>
								<option>Canada</option>
								<option>Mexico</option>
							</select>
						</div>

						<div class="col-span-6">
							<label for="street-address" class="block text-sm font-medium text-gray-700"
								>Street address</label
							>
							<input
								type="text"
								name="street-address"
								id="street-address"
								autocomplete="street-address"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>

						<div class="col-span-6 sm:col-span-6 lg:col-span-2">
							<label for="city" class="block text-sm font-medium text-gray-700">City</label>
							<input
								type="text"
								name="city"
								id="city"
								autocomplete="address-level2"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>

						<div class="col-span-6 sm:col-span-3 lg:col-span-2">
							<label for="region" class="block text-sm font-medium text-gray-700"
								>State / Province</label
							>
							<input
								type="text"
								name="region"
								id="region"
								autocomplete="address-level1"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>

						<div class="col-span-6 sm:col-span-3 lg:col-span-2">
							<label for="postal-code" class="block text-sm font-medium text-gray-700"
								>ZIP / Postal code</label
							>
							<input
								type="text"
								name="postal-code"
								id="postal-code"
								autocomplete="postal-code"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>
						<!-- add an input for entering the preferred price-->
						<div>
							<label for="price" class="block text-sm font-medium text-gray-700"
								>Preferred Price</label
							>
							<div class="mt-1 relative rounded-md shadow-sm">
								<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
									<span class="text-gray-500 sm:text-sm"> $ </span>
								</div>
								<input
									type="text"
									name="price"
									id="price"
									class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-7 pr-12 sm:text-sm border-gray-300 rounded-md"
									placeholder="0.00"
									aria-describedby="price-currency"
								/>
								<div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
									<span class="text-gray-500 sm:text-sm" id="price-currency"> USD </span>
								</div>
							</div>
						</div>
						<!-- add date selection for preffered completion date-->
						<div class="col-span-6 sm:col-span-3 lg:col-span-2">
							<label for="date" class="block text-sm font-medium text-gray-700"
								>Preferred Completion Date</label
							>
							<input
								type="date"
								name="date"
								id="date"
								autocomplete="date"
								class="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
							/>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>

	<div class="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
		<div class="md:grid md:grid-cols-3 md:gap-6">
			<div class="md:col-span-1">
				<h3 class="text-lg font-medium leading-6 text-gray-900">Notifications</h3>
				<p class="mt-1 text-sm text-gray-500">Decide which communications you'd like to receive.</p>
			</div>
			<div class="mt-5 md:mt-0 md:col-span-2">
				<form class="space-y-6" action="#" method="POST">
					<fieldset>
						<legend class="text-base font-medium text-gray-900">By Email</legend>
						<div class="mt-4 space-y-4">
							<div class="flex items-start">
								<div class="h-5 flex items-center">
									<input
										id="comments"
										name="comments"
										type="checkbox"
										class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
									/>
								</div>
								<div class="ml-3 text-sm">
									<label for="comments" class="font-medium text-gray-700">Comments</label>
									<p class="text-gray-500">
										Get notified when someone posts a comment on a posting.
									</p>
								</div>
							</div>
							<div class="flex items-start">
								<div class="flex items-center h-5">
									<input
										id="candidates"
										name="candidates"
										type="checkbox"
										class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
									/>
								</div>
								<div class="ml-3 text-sm">
									<label for="candidates" class="font-medium text-gray-700">Bids</label>
									<p class="text-gray-500">Get notified when there is a new bid for the auction.</p>
								</div>
							</div>
							<div class="flex items-start">
								<div class="flex items-center h-5">
									<input
										id="offers"
										name="offers"
										type="checkbox"
										class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
									/>
								</div>
								<div class="ml-3 text-sm">
									<label for="offers" class="font-medium text-gray-700">Buyout offers</label>
									<p class="text-gray-500">Get notified when a receive a new buyout offer.</p>
								</div>
							</div>
						</div>
					</fieldset>
				</form>
			</div>
		</div>
	</div>

	<div class="flex justify-end">
		<button
			type="button"
			class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
			>Cancel</button
		>
		<button
			type="submit"
			class="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
			>Save</button
		>
	</div>
</div>
