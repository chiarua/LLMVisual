import { GroupBy } from './query/groupby';
/**
 * An ordered tree structure for storing query results.
 */
export interface ResultTree<T> {
    name: string;
    path: string;
    items: (ResultTree<T> | T)[];
    groupBy?: GroupBy;
    orderGroupBy?: string | string[];
}
export declare function isResultTree<T>(item: ResultTree<T> | T): item is ResultTree<T>;
export declare function getTopResultTreeItem<T>(specQuery: ResultTree<T>): T;
export declare function mapLeaves<T, U>(group: ResultTree<T>, f: (item: T) => U): ResultTree<U>;
