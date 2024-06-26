import { Icon } from "@iconify/react/dist/iconify.js";

export const InstitutionModal = ({
  closeModal,
  institutionID,
}: {
  closeModal: () => void;
  institutionID: string;
}) => {
  return (
    <div className="fixed top-0 left-0 w-screen h-screen flex items-center justify-center bg-black/25">
      <div className="relative w-full max-w-2xl h-72 p-4 md:p-8 flex flex-col gap-8 rounded-md bg-white">
        <button
          className="absolute top-0 right-0 p-2 text-2xl hover:text-red-700"
          onClick={closeModal}
        >
          <Icon icon="material-symbols:close" />
        </button>
        <div className="w-full">
          <h2 className="text-xl md:text-2xl font-bold">College of Science and Technology</h2>
          <p className="md:text-lg font-medium">MoonCity, MoonState</p>
        </div>
        <div className="w-full">
            <p>Subjects Taught: 100</p>
            <p>Lessons published: 100</p>
            <p>Number of students: 100</p>
        </div>
        <button className="w-24 h-8 self-end flex items-center justify-center p-2 bg-blue-200 hover:bg-blue-700 rounded-md hover:text-white">
          <Icon icon="material-symbols:delete-outline" /> Delete
        </button>
      </div>
    </div>
  );
};
