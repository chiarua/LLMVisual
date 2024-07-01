import { Query } from './query';
/**
 * Normalize the non-nested version of the query
 * (basically when you have a `groupBy`)
 * to a standardize nested.
 */
export declare function normalize(q: Query): Query;
