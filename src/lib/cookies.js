import { parse } from 'cookie';

export function getCookie(name) {
	const cookie = parse(document.cookie)[name];
	return cookie ? decodeURIComponent(cookie) : null;
}
