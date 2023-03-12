import { supabase } from '../lib/supabaseClient.js';

export async function sessionMiddleware(request, next) {
	const { data: session, error } = await supabase.auth.api.getUserByCookie(request.headers.cookie);

	if (error) {
		// There was an error getting the session
		console.error(error);
	} else {
		// Add the session to the request object
		request.locals.session = session;
	}

	// Call the next function in the middleware chain
	return {
		session: session.session
	};
}
