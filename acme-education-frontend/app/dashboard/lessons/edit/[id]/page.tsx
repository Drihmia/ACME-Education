"use client";

import { LessonForm } from "@/app/ui/dashboard/lessonForm";

export default function Page({ params }: { params: { id: string } }) {
  return (<LessonForm action="Edit" id={params.id} />)
}
