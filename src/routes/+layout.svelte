<script>
	import '../app.css';
</script>

<svelte:head>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap');
		/* import Golos text font */
		@import url('https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700;800;900&display=swap');
	</style>
	<link
		href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.3/flowbite.min.css"
		rel="stylesheet"
	/>
</svelte:head>

<main>
	<button
		data-drawer-target="default-sidebar"
		data-drawer-toggle="default-sidebar"
		aria-controls="default-sidebar"
		type="button"
		class="inline-flex items-center p-2 mt-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
	>
		<span class="sr-only">Open sidebar</span>
		<svg
			class="w-6 h-6"
			aria-hidden="true"
			fill="currentColor"
			viewBox="0 0 20 20"
			xmlns="http://www.w3.org/2000/svg"
		>
			<path
				clip-rule="evenodd"
				fill-rule="evenodd"
				d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"
			/>
		</svg>
	</button>

	<aside
		id="default-sidebar"
		class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
		aria-label="Sidebar"
	>
		<div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
			<ul class="space-y-2">
				<li>
					<a
						href="/"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-magnifying-glass-dollar fa-lg" />
						<span class="ml-3">Browse listings</span>
					</a>
				</li>
				<li>
					<a
						href="/auctions"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-list fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">My auctions</span>
					</a>
				</li>
				<li>
					<a
						href="/"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-plus fa-lg" /><span class="flex-1 ml-3 whitespace-nowrap"
							>New auction</span
						>
					</a>
				</li>
				<li>
					<a
						href="/"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-envelope fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">Notifications</span>
						<span
							class="inline-flex items-center justify-center w-3 h-3 p-3 ml-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300"
							>3</span
						>
					</a>
				</li>
				<li>
					<a
						href="/"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-users fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">Customers</span>
					</a>
				</li>

				<li>
					<a
						href="/auth/login"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-right-to-bracket fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">Log In</span>
					</a>
				</li>
				<li>
					<a
						href="/auth/register"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-user-plus fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">Register</span>
					</a>
				</li>
				<li>
					<a
						href="/auth/signout"
						class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
					>
						<i class="fa-solid fa-list fa-lg" />
						<span class="flex-1 ml-3 whitespace-nowrap">Sign out</span>
					</a>
				</li>
			</ul>
		</div>
	</aside>
	<slot />
</main>

<style>
	main {
		display: flexbox;
		height: 100%;
		width: 100%;
		place-items: center;
		align-items: center;
		/*background: linear-gradient(-135deg, #c850c0, #4158d0); */
	}

	/* set font family */
	* {
		font-family: 'Golos text', sans-serif;
	}
</style>
