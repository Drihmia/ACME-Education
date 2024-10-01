import Cookies from 'js-cookie'


export const fetcher = (args: string) => fetch(args).then(res => res.json())

export const deleteLesson = async (lessonId: string) => {
  try {
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    }

    // Getting csrfToken from cookies and send them with fetch post request.
    const csrfToken = Cookies.get('csrf_access_token');
    
    if (csrfToken) {
      headers['X-CSRF-TOKEN'] = csrfToken;
    }

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/lessons/${lessonId}`,
        {
        method: "DELETE",
        headers: headers,
      }
    );

    return response.json()
  } catch (e) {
    return "Somethig went wrong"
  }
}
