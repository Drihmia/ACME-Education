import { useAuth } from "@/app/context/authContext";
import { deleteLesson } from "@/app/lib/fetch";
import { lessonFormProps } from "@/app/types";
import { Icon } from "@iconify/react/dist/iconify.js";
import Link from "next/link";
import { mutate } from "swr";
import DOMPurify from "dompurify";

export const LessonModal = ({
  closeModal,
  item,
}: {
  closeModal: () => void;
  item: lessonFormProps;
}) => {
  const { user } = useAuth()!;

  const downloadLink = (previewLink: string) => {
    const lessonId = previewLink.split('/')?.[5];
    console.log('lessonId:', lessonId);
      return `https://drive.usercontent.google.com/download?id=${lessonId}&export=download`;
  };

  const sanitizedDescription = DOMPurify.sanitize(item.description);

  return (
    <div className="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-black/25">
      <div className="relative w-full max-w-2xl h-[512px] overflow-y-scroll p-4 md:p-8 flex flex-col justify-between rounded-md bg-white">
        <button
          className="absolute top-0 right-0 p-2 text-2xl hover:text-red-700"
          onClick={closeModal}
        >
          <Icon icon="material-symbols:close" />
        </button>
        <div className="w-full grid gap-4 md:gap-8">
          <div className="w-full">
            <h2 className="text-2xl md:text-3xl font-bold">{item.name}</h2>
            <p className="text-lg md:text-xl font-medium">
              {item.subject}
            <p className="text-lg md:text-xl font-medium">By {item.teacher}</p>
            </p>
          </div>
          <article className="w-full">
            <h3 className="text-xl md:text-2xl font-semibold">Description</h3>
            <p dangerouslySetInnerHTML={{ __html: sanitizedDescription }} ></p>
            <div className="grid">
              {/*<Link href={item.download_link} target="_blank" className="text-blue-500 underline">
                Preview lesson
              </Link> */}
              { item.download_link.includes("drive.google.com") ?
                (
                  <Link href={downloadLink(item.download_link)} target="_blank" className="text-blue-500 underline">
                    Download lesson
                  </Link>
              ) : (
                <Link href={item.download_link} target="_blank" className="text-blue-500 underline">
                  View lesson
                </Link>
              )
              }
            </div>
          </article>
        </div>
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
                      `${process.env.NEXT_PUBLIC_API_ADDRESS}/api/v1/teachers/${item.teacher_id}/lessons`
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
