export const fetcher = (args: string) => fetch(args).then(res => res.json())

export const deleteLesson = async (lessonId: string) => {
    try {
        const response = await fetch(
          `http://127.0.0.1:5000/api/v1/lessons/${lessonId}`,
          {
            method: "DELETE"
          }
        );

        return response.json()
    } catch (e) {
        return "Somethig went wrong"
    }
}
