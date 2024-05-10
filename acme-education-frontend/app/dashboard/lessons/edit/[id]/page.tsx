"use client";

import { useAuth } from "@/app/context/authContext";
import { LessonForm } from "@/app/ui/dashboard/lessonForm";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import Cookies from 'js-cookie'

export default function Page({ params }: { params: { id: string } }) {
  const router = useRouter();

  useEffect(() => {
    const user = JSON.parse(Cookies.get("currentUser")!)
    
    if (user && user.class != "Teacher") {
      alert(`You do not have permission to access this route.`);
      router.push("/dashboard");
    }
  }, []);
  return (<LessonForm action="Edit" id={params.id} />)
}
