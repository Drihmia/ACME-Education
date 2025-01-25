import { Form, Formik, useField, useFormik, useFormikContext } from "formik";
import { filterSchema } from "../validation/filter";
import { FieldSet, MyTextAndSelectInput, MyTextInput } from "./form";
import { lessonFormProps, subjectProps } from "../types";
import { useState } from "react";
import { LessonCard } from "./dashboard/lessonsCard";

interface filterFormProps {
  subjects: subjectProps[];
  lessons: lessonFormProps[];
  openModal: (val: string) => void;
  user_class: string
}

export const FilterForm = ({
  subjects,
  lessons,
  openModal,
  user_class
}: filterFormProps) => {
  const [filteredLessons, setFilteredLessons] = useState(lessons)

  //console.log("User Class:", user_class)

  const applyFilter = (values: {
    teacher: string;
    subject: string;
    name: string;
    public: string;
    lesson: string;
    institution: string;
  }) => {
    const regexLessonName = new RegExp(values.name, "gi");
    const regexTeacherName = new RegExp(values.teacher, "gi");
    const regexLessonClass = new RegExp(values.lesson, "gi");
    const regexLessonInstitution = new RegExp(values.institution, "gi");
    //console.log("values.institutions:", values.institution)

    const data = lessons
      .filter((lesson) => { // Search by lesson's name
        if (values.name === "") return lesson;
        if (regexLessonName.test(lesson.name)) return lesson;
      })
      .filter((lesson) => { // Search by lesson's subject
        if (values.subject === "") return lesson;

        const subject = subjects.find((sub) => sub.name === values.subject);
        if (lesson.subject_id === subject?.id) return lesson;
      })
      .filter((lesson) => { // Search by testing lesson's public state, public or private 
        if (values.public === "") return lesson;
        if (lesson.public && values.public === "true") return lesson;
        if (!lesson.public && values.public === "false") return lesson;
      })
      .filter((lesson) => { // Search by matching lesson's author (Teacher) - For Students 
        if (values.teacher === "") return lesson;
        const regexTeacherName = new RegExp(values.teacher, "i");
        if (regexTeacherName.test(lesson.teacher || "")) return lesson;
      })
      .filter((lesson) => { // Search by matching lesson's class alias.
        if (values.lesson === "") return lesson;
        if (regexLessonClass.test(lesson.class_alias!)) return lesson;
      })
      .filter((lesson) => { // Search by matching one of lesson's institution names
        if (values.institution === "") return lesson;

        // I've used a fresh regex without 'g' flag to avoid a random behaviour from subsequet calls.
        const hasMatchingInstitution = (lesson.institutions ?? []).some((institution_name) => {
          // Fresh regex, with no 'g' flag, for each check
          const regexLessonInstitution = new RegExp(values.institution, "i");
          return regexLessonInstitution.test(institution_name);
        });

        if (hasMatchingInstitution) return lesson;
      });

    setFilteredLessons(data);
  };

  const gridColumnsTeacher = "w-full grid gap-4 lg:grid-cols-[2fr_2fr_2fr_2fr_2fr_1fr] lg:gap-6 lg:items-center"
  const gridColumnsStudent = "w-full grid gap-4 lg:grid-cols-[2fr_2fr_2fr_2fr_1fr] lg:gap-6 lg:items-center"
  return (
    <>
    <div className="w-full">
      <p className="font-semibold text-lg mt-4">Filter By</p>
      <Formik
        initialValues={{
          teacher: "",
          subject: "",
          name: "",
          public: "",
          lesson: "",
          institution: "",
        }}
        validationSchema={filterSchema}
        onSubmit={(values, { setSubmitting }) => {
          //console.log(`Values from onSubmit`)
          //console.table(values)
          applyFilter(values);
          setSubmitting(false);
        }}
        onReset={(values, { resetForm }) => {
          values = {
            teacher: "",
            subject: "",
            name: "",
            public: "",
            lesson: "",
            institution: "",
          };
          setFilteredLessons(lessons)
        }}
      >
        {({ values }) => (
          <Form
            className={ `${user_class === 'Teacher' ? gridColumnsTeacher : gridColumnsStudent }` }
          >
            <MyTextAndSelectInput
              label="Subject"
              name="subject"
              data={subjects}
              type="text"
              placeholder="e.g Physique-Chimie"
              optional={true}
            />
            <MyTextInput
            label="Name"
            name="name"
            type="text"
            placeholder="Chemical Transformations"
            />
            { user_class === "Student" && <MyTextInput
              label="Teacher"
              name="teacher"
              type="text"
              placeholder="DRIHMIA REDOUANE"
            />
            }
            { user_class === "Teacher" &&
              <MyTextInput
                label="Class"
                name="lesson"
                type="text"
                placeholder="1BAC Fr"
              />
            }
            { user_class === "Teacher" &&
              <MyTextInput
                label="Institution"
                name="institution"
                type="text"
                placeholder="Lycee Qualifiant ALMANDAR ALJAMIL"
              />
            }
          <FieldSet
            label="Public"
            name="public"
            options={[
              {
                name: "public",
                label: "Yes",
                value: true,
                type: "radio",
                checked: values.public === "true" ? true : false
              },
              {
                name: "public",
                label: "No",
                value: false,
                type: "radio",
                checked: values.public === "false" ? true : false
              },
            ]}
          />
          <div className="flex items-center gap-2">
            <button
              type="submit"
              className="w-28 h-12 py-2 bg-blue-100 text-black hover:text-white hover:bg-blue-700 capitalize rounded-xl"
            >
              Apply filter
            </button>
            <button
              type="reset"
              className="w-20 h-12 py-2 bg-red-100 text-black hover:text-white hover:bg-red-600 capitalize rounded-xl"
            >
              Clear
            </button>
          </div>
        </Form>
        )}
      </Formik>
    </div>
    {filteredLessons.length > 0 ? (
      <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
        <li className="w-full grid grid-cols-[0.75fr_5fr_2fr_2fr_0.5fr] p-2 bg-blue-50 rounded-md">
          <span className="font-semibold">S/N</span>
          <span className="font-semibold">Title</span>
          <span className="font-semibold">Subject</span>
          <span className="font-semibold">Author</span>
          <span className="font-semibold">Public</span>
        </li>
        {filteredLessons.map((lesson: lessonFormProps, i: number) => (
          <LessonCard
            key={`${i}`}
            index={i}
            lesson={lesson}
            openModal={openModal}
            user_class={user_class}
          />
        ))}
      </ul>
    ) : (
      <p>You do not have any published lessons.</p>
    )}
    </>
  );
};
