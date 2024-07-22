"use client";

import { LessonForm } from "@/app/ui/dashboard/lessonForm";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import Cookies from 'js-cookie'

export default function Page() {
  const router = useRouter();

  useEffect(() => {
    const user = JSON.parse(Cookies.get("currentUser")!)
    
    if (user && user.class != "Teacher") {
      alert(`You do not have permission to access this route.`);
      router.push("/dashboard");
    }
  }, [router]);

  return <LessonForm action="Add" />;
}
