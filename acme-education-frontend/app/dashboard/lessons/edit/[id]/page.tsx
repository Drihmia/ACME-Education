"use client";

import { useAuth } from "@/app/context/authContext";
import { LessonForm } from "@/app/ui/dashboard/lessonForm";
import { useRouter } from "next/navigation";

export default function Page({ params }: { params: { id: string } }) {
  const { user } = useAuth()!
  const router = useRouter()

  if (user?.class != "Teacher") {
    alert("You do not have permission to access this route.")
    router.push("/dashboard")
  }
  return (<LessonForm action="Edit" id={params.id} />)
}
