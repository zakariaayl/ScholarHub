import { motion } from "framer-motion";
import { ExternalLink } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export interface SearchResult {
  id: string;
  title: string;
  description: string;
  source: string;
  url: string;
}

interface ResultCardProps {
  result: SearchResult;
  index: number;
}

const ResultCard = ({ result, index }: ResultCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: index * 0.1 }}
    >
      <Card className="h-full hover:shadow-lg transition-all duration-200 hover:border-primary/50 bg-card group">
        <CardHeader>
          <div className="flex items-start justify-between gap-2">
            <CardTitle className="text-xl group-hover:text-primary transition-colors duration-200">
              <a
                href={result.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2 hover:underline"
              >
                {result.title}
                <ExternalLink className="h-4 w-4 opacity-0 group-hover:opacity-100 transition-opacity" />
              </a>
            </CardTitle>
          </div>
          <Badge variant="secondary" className="w-fit">
            {result.source}
          </Badge>
        </CardHeader>
        <CardContent>
          <CardDescription className="text-sm leading-relaxed">
            {result.description}
          </CardDescription>
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default ResultCard;
