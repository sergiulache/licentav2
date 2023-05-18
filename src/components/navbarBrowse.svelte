<script>
	import { current } from '../stores/currentNav';

	function handleClick(path) {
		$current = path;
	}
</script>

<li
	class="hover:-translate-y-1 hover:scale-105 hover:border-indigo-400 border-b-2 rounded-lg duration-300 "
>
	<a
		href="/browse"
		class:active={$current === '/browse'}
		on:click={() => handleClick('/browse')}
		class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors "
	>
		<i class="fa-solid fa-magnifying-glass-dollar fa-lg  text-gray-600" />
		<span class="ml-3 flex items-center flex-nowrap  text-gray-600">Browse listings</span>
	</a>
</li>

<li
	class="hover:-translate-y-1 hover:scale-105 hover:border-indigo-400 border-b-2 rounded-lg duration-300 "
>
	<a
		href="/test"
		class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"
	>
		<i class="fa-solid fa-magnifying-glass-dollar fa-lg  text-gray-600" />
		<span class="ml-3  text-gray-600">Test</span>
	</a>
</li>

<style>
	.active {
		background-color: #b8d0ea;
		color: white;
	}
</style>
