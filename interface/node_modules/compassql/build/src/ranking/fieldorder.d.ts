import { QueryConfig } from '../config';
import { SpecQueryModel } from '../model';
import { Schema } from '../schema';
import { RankingScore } from './ranking';
export declare const name = "fieldOrder";
/**
 * Return ranking score based on indices of encoded fields in the schema.
 * If there are multiple fields, prioritize field on the lower indices of encodings.
 *
 * For example, to compare two specs with two encodings each,
 * first we compare the field on the 0-th index
 * and only compare the field on the 1-th index only if the fields on the 0-th index are the same.
 */
export declare function score(specM: SpecQueryModel, schema: Schema, _: QueryConfig): RankingScore;
