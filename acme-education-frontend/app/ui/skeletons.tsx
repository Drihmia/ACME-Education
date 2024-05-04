export const ProfileSkeleton = () => {
  return (
    <div className="w-full grid gap-4">
      <div className="w-full grid gap-1">
        <h1 className={`w-64 h-12 rounded animate-pulse bg-gray-300`}></h1>
        <span className="block w-96 h-8 rounded animate-pulse bg-gray-300"></span>
      </div>
      <div className="w-full grid md:grid-cols-2 gap-4 md:gap-8 mt-8">
        <div className="w-full flex items-center justify-center animate-pulse">
          <div className="w-64 h-64 bg-gray-300 rounded-md"></div>
        </div>
        <div className="w-full flex flex-col gap-2">
          <h2 className="w-36 h-10 rounded animate-pulse bg-gray-300"></h2>
          <ul className="w-full flex flex-col gap-1">
            <li className="w-60 h-8  mt-4 rounded animate-pulse bg-gray-300"></li>
            <li className="w-60 h-8  mt-4 rounded animate-pulse bg-gray-300"></li>
            <li className="w-60 h-8  mt-4 rounded animate-pulse bg-gray-300"></li>
            <li className="w-60 h-8  mt-4 rounded animate-pulse bg-gray-300"></li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export const LessonCardSkeleton = () => (
  <li className={`w-full h-8 rounded animate-pulse bg-gray-300`}></li>
);

export const LessonsSkeleton = () => (
  <div className="w-full grid gap-4">
      <h1 className={`w-64 h-12 rounded animate-pulse bg-gray-300`}></h1>
      <div className="w-full flex flex-col gap-2">
        <div className="w-full flex items-center justify-between py-4">
          <h2 className="w-96 h-8 rounded animate-pulse bg-gray-300"></h2>
          <p className="w-48 h-8 rounded animate-pulse bg-gray-300"></p>
        </div>
        <ul className="w-full flex flex-col gap-2 pt-4 pb-12">
          {Array.from({ length: 5 }).map((_, i) => (
            <LessonCardSkeleton key={`${i}`} />
          ))}
        </ul>
      </div>
    </div>
)