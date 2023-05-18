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
		href="/auth/login"
		class:active={$current === '/auth/login'}
		on:click={() => handleClick('/auth/login')}
		class="flex items-center p-2 pr-28 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors duration-600"
	>
		<i class="fa-solid fa-right-to-bracket fa-lg text-gray-600" />
		<span class="flex-1 ml-3 whitespace-nowrap">Log In</span>
	</a>
</li>

<style>
	.active {
		background-color: #b8d0ea;
		color: white;
	}
</style>
