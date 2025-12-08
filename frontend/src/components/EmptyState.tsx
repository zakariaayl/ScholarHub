import { motion } from "framer-motion";
import { SearchX } from "lucide-react";

const EmptyState = () => {
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      className="flex flex-col items-center justify-center py-16 gap-4"
    >
      <SearchX className="h-16 w-16 text-muted-foreground/50" />
      <div className="text-center">
        <h3 className="text-xl font-semibold mb-2">No results found</h3>
        <p className="text-muted-foreground">
          Try adjusting your search terms or filters
        </p>
      </div>
    </motion.div>
  );
};

export default EmptyState;