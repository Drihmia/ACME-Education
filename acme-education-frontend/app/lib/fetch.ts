export const fetcher = (args: string) => fetch(args).then(res => res.json())

export const deleteLesson = async (lessonId: string) => {
    try {
        const response = await fetch(
          `http://${process.env.NEXT_API_ADDRESS}/api/v1/lessons/${lessonId}`,
          {
            method: "DELETE"
          }
        );

        return response.json()
    } catch (e) {
        return "Somethig went wrong"
    }
}
