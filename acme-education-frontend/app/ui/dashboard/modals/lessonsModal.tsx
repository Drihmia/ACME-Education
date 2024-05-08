import { useAuth } from "@/app/context/authContext";
import { deleteLesson } from "@/app/lib/fetch";
import { lessonFormProps } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import Link from "next/link";
import { mutate } from "swr";

export const LessonModal = ({
  closeModal,
  item,
}: {
  closeModal: () => void;
  item: lessonFormProps;
}) => {
  const { user } = useAuth()!;

  return (
    <div className="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-black/25">
      <div className="relative w-full max-w-2xl min-h-96 p-4 md:p-8 flex flex-col justify-between gap-8 rounded-md bg-white">
        <button
          className="absolute top-0 right-0 p-2 text-2xl hover:text-red-700"
          onClick={closeModal}
        >
          <Icon icon="material-symbols:close" />
        </button>
        <div className="w-full">
          <h2 className="text-2xl md:text-3xl font-bold">{item.name}</h2>
          <p>{item.teacher_id}</p>
          <p className="text-lg md:text-xl font-semibold">
            {item.institution_id}
          </p>
        </div>
        <article className="w-full">
          <h3 className="text-xl md:text-2xl font-bold">Description</h3>
          <p>{item.description}</p>
          <Link href={item.download_link} className="text-blue-500 underline">
            Download lesson
          </Link>
        </article>
        {user?.class === "Teacher" && (
          <div className="w-full self-end flex items-center gap-2">
            <Link
              href={`/dashboard/lessons/edit/${item.id}`}
              className="w-24 h-8 flex items-center justify-center p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white"
            >
              <Icon icon="akar-icons:edit" /> Edit
            </Link>
            <button
              onClick={async () => {
                if (confirm("Are you sure you delete this lesson?")) {
                  const res = await deleteLesson(item.id!);
                  if (res["error"]) {
                    alert("Something went wrong.");
                  } else {
                    mutate(
                      `http://127.0.0.1:5000/api/v1/teachers/${item.teacher_id}/lessons`
                    );
                    alert("Lesson deleted");
                    closeModal();
                  }
                }
              }}
              className="w-24 h-8 flex items-center justify-center p-2 bg-red-200 hover:bg-red-700 rounded-md hover:text-white"
            >
              <Icon icon="material-symbols:delete-outline" /> Delete
            </button>
          </div>
        )}
      </div>
    </div>
  );
};
