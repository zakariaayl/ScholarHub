import { motion } from "framer-motion";
import { SearchX } from "lucide-react";

const EmptyState = () => {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      className="flex flex-col items-center justify-center py-16 gap-4"
    >
      <div className="rounded-full bg-muted p-6">
        <SearchX className="h-12 w-12 text-muted-foreground" />
      </div>
      <div className="text-center">
        <h3 className="text-lg font-semibold mb-2">No results found</h3>
        <p className="text-muted-foreground text-sm max-w-md">
          We couldn't find any results matching your search. Try different keywords or filters.
        </p>
      </div>
    </motion.div>
  );
};

export default EmptyState;
